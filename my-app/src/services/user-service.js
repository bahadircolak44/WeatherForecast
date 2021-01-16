import client from "../client";

class UserService {
    login(payload) {
        return client.post("auth/login/", payload);
    }

    register(payload) {
        return client.post("auth/register/", payload);
    }

    logout() {
        return client.post("auth/logout/");
    }

    userDetail() {
        return client.get("auth/me/");
    }

    cities() {
        return client.get("cities/");
    }

    weather(payload) {
        return client.post("weather-forecast/", payload);
    }

    getWeather(payload) {
        return client.post("weather-forecast/", payload)
            .then(res => res.json());
    }
}

export default new UserService();