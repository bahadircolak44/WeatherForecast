import client from "../client";

class UserService {
  login(payload) {
    console.log("TEST")
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
}

export default new UserService();