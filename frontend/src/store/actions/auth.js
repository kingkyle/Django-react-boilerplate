import axios from "axios";
import { tokenConfig } from "../config";
import {
  AUTH_SUCCESS,
  AUTH_LOADING,
  AUTH_FAIL,
  AUTH_VERIFIED,
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGOUT_SUCCESS
} from "./types";

export const login = (username, password) => dispatch => {
  dispatch({ type: AUTH_LOADING });
  const config = {
    headers: {
      "content-type": "application/json"
    }
  };
  const body = JSON.stringify({ username, password });
  axios
    .post("/api/auth/login/", body, config)
    .then(res =>
      dispatch({
        type: AUTH_SUCCESS,
        payload: res.data
      })
    )
    .catch(err => {
      console.log(err);
      dispatch({
        type: AUTH_FAIL
      });
    });
};

export const register = (username, password) => dispatch => {
  dispatch({ type: AUTH_LOADING });
  const config = {
    headers: {
      "content-type": "application/json"
    }
  };
  const body = JSON.stringify({ username, password });
  axios
    .post("/api/auth/register/", body, config)
    .then(res => dispatch({ type: REGISTER_SUCCESS, payload: res.data }))
    .catch(err => dispatch({ type: REGISTER_FAIL }));
};

export const loadUser = () => (dispatch, getState) => {
  dispatch({ type: AUTH_LOADING });
  axios
    .get("/api/auth/verify-user", tokenConfig(getState))
    .then(res => {
      if (res.data.id === null) {
        dispatch({ type: AUTH_FAIL });
      } else {
        dispatch({ type: AUTH_VERIFIED, payload: res.data });
      }
    })
    .catch(err => dispatch({ type: AUTH_FAIL }));
};

export const logout = () => (dispatch, getState) => {
  dispatch({ type: AUTH_LOADING });
  axios
    .post("/rest-auth/logout/", tokenConfig(getState))
    .then(res => dispatch({ type: LOGOUT_SUCCESS }))
    .catch(err => dispatch({ type: AUTH_FAIL }));
};
