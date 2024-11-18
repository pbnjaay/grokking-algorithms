import requests
import logging
import structlog


class ApiException(Exception):
    """Exception de base pour les erreurs API."""
    pass


class BadRequestException(ApiException):
    """Exception pour une erreur 400 Bad Request."""
    pass


class UnauthorizedException(ApiException):
    """Exception pour une erreur 401 Unauthorized."""
    pass


class ForbiddenException(ApiException):
    """Exception pour une erreur 403 Forbidden."""
    pass


class NotFoundException(ApiException):
    """Exception pour une erreur 404 Not Found."""
    pass


class ServerErrorException(ApiException):
    """Exception pour une erreur 5xx Server Error."""
    pass


class TokenRefreshException(ApiException):
    """Exception pour une erreur sur le renouvellement de token."""
    pass


class Result:
    def __init__(self, code, data):
        self.code = code
        self.data = data if data else []


class ApiService:
    def __init__(self, base_url, service_name, logger, headers=None, timeout=10, refresh_token_callback=None, token_type='Bearer'):
        """
        Initialise le service API.

        :param base_url: URL de base pour les appels API.
        :param service_name: Nom du service (pour la journalisation).
        :param headers: Dictionnaire des en-têtes par défaut.
        :param timeout: Délai d'expiration par défaut pour les requêtes.
        :param refresh_token_callback: Fonction pour rafraîchir le token.
        :param token_type: Le type de token d'auhentification
        :param logger: Logger structlog.
        """
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update(headers or {})
        self.timeout = timeout
        self.service_name = service_name
        self.refresh_token_callback = refresh_token_callback
        self.token_type = token_type
        self.logger = logger

    def _set_auth_token(self, token):
        """
        Met à jour le token d'authentification dans les en-têtes de la session.
        """
        self.session.headers["Authorization"] = f"{self.token_type} {token}"
        self.logger.info(
            "Token d'authentification mis à jour dans la session.")

    def _refresh_token(self):
        """
        Rafraîchit le token d'authentification.
        """
        if not self.refresh_token_callback:
            self.logger.error(
                "Aucun callback de renouvellement de token défini.")
            raise TokenRefreshException("Impossible de renouveler le token.")

        self.logger.info("Renouvellement du token d'authentification...")
        new_token = self.refresh_token_callback()
        if not new_token:
            raise TokenRefreshException("Le renouvellement du token a échoué.")
        self._set_auth_token(new_token)

    def _log_request(self, method, url, **kwargs):
        """
        Log les informations de la requête.

        :param method: Méthode HTTP (GET, POST, etc.).
        :param url: URL complète de la requête.
        :param kwargs: Paramètres de la requête (headers, params, etc.).
        """
        self.logger.debug(f"{self.service_name} - {method} - Request", url=url)
        self.logger.debug(f"{self.service_name} - {method} - Request",
                          headers={kwargs.get('headers')})
        self.logger.debug(f"{self.service_name} - {method} - Request",
                          params={kwargs.get('params')})
        self.logger.debug(f"{self.service_name} - {method} - Request",
                          data={kwargs.get('data')})
        self.logger.debug(f"{self.service_name} - {method} - Request",
                          json={kwargs.get('json')})

    def _log_response(self, response):
        """
        Log les informations de la réponse.

        :param response: L'objet Response de requests.
        """
        self.logger.info(
            f"{self.service_name} - Response", status_code=response.status_code, url=response.url)
        self.logger.debug(
            f"{self.service_name} - Response", response=response.text)

    def _handle_response(self, response) -> Result:
        """
        Gère les réponses des requêtes et lève les exceptions appropriées.

        :param response: L'objet Response de requests.
        :return: Le contenu JSON si la réponse est valide.
        :raises: Une exception personnalisée en cas d'erreur.
        """
        self._log_response(response)
        if 400 <= response.status_code < 500:
            if response.status_code == 400:
                raise BadRequestException(
                    f"Bad Request: {response.text}")
            elif response.status_code == 401:
                raise UnauthorizedException(
                    f"Unauthorized: {response.text}")
            elif response.status_code == 403:
                raise ForbiddenException(
                    f"Forbidden: {response.text}")
            elif response.status_code == 404:
                raise NotFoundException(
                    f"Not Found: {response.text}")
            else:
                raise ApiException(
                    f"Client Error {response.status_code}: {response.text}")

        if 500 <= response.status_code < 600:
            raise ServerErrorException(
                f"{self.service_name} - Server Error {response.status_code}: {response.text}")

        try:
            return Result(code=response.status_code, data=response.json())
        except ValueError:
            logging.error("Impossible de décoder le JSON: %s", e)
            raise ApiException("Réponse non valide reçue.")

    def _request_with_token_refresh(self, method, url, **kwargs):
        """
        Gère les requêtes avec tentative de renouvellement du token en cas d'erreur 401.
        """
        try:
            response = self.session.request(
                method, url, timeout=self.timeout, **kwargs)
            return self._handle_response(response)
        except UnauthorizedException:
            self.logger.warning(
                f"{self.service_name} - Token expiré, tentative de renouvellement...")
            self._refresh_token()
            response = self.session.request(
                method, url, timeout=self.timeout, **kwargs)
            return self._handle_response(response)

    def get(self, endpoint, params=None):
        """
        Effectue une requête GET.

        :param endpoint: Le chemin de l'API (par exemple "/users").
        :param params: Les paramètres de la requête GET.
        :return: Le résultat de la réponse.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        method = "GET"
        try:
            self._log_request(method, url, params=params)
            return self._request_with_token_refresh(method, url, params=params)
        except Exception as e:
            self.logger.error(
                f'{self.service_name} _ {method} request failed: {e}')
            raise ApiException(
                f'{self.service_name} _ {method} request failed: {e}') from e

    def post(self, endpoint, data=None, json_data=None):
        """
        Effectue une requête POST.

        :param endpoint: Le chemin de l'API (par exemple "/users").
        :param data: Les données de formulaire ou en brut.
        :param json_data: Les données JSON à envoyer.
        :return: Le résultat de la réponse.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        method = "POST"
        try:
            self._log_request(method, url, data=data, json=json_data)
            return self._request_with_token_refresh(method, url, data=data, json=json_data)
        except Exception as e:
            self.logger.error(
                f"{self.service_name} - {method} request failed: {e}")
            raise ApiException(
                f"{self.service_name} - {method} request failed: {e}") from e


logger = structlog.get_logger('wz-log')


def mock_refresh_token():
    return "new_access_token"


try:
    base_url = 'https://jsonplaceholder.typicode.com'
    service = ApiService(
        base_url,
        service_name='SAAR_ASSURANCE',
        refresh_token_callback=mock_refresh_token,
        logger=logger
    )
    res = service.get('/posts/1')
    print(res.data)
except ApiException as e:
    print(e)
