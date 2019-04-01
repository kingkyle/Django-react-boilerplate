export const tokenConfig = getState => {
  // Get token from state
  const token = getState().auth.token;
  // send Headers
  const config = {
    headers: {
      "content-type": "application/json"
    }
  };
  if (token) {
    config.headers["Authorization"] = `Token ${token}`;
  }
  return config;
};
