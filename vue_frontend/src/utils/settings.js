export default {
    CSRF_TOKEN: document.getElementsByName("csrfmiddlewaretoken")[0].value,
    API_ROOT_URL: document.location.origin.toString() + '/api/',

}