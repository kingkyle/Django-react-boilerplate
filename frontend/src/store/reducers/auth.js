import {
  AUTH_FAIL,
  AUTH_LOADING,
  AUTH_SUCCESS,
  LOGOUT_SUCCESS,
  AUTH_VERIFIED,
  REGISTER_FAIL,
  REGISTER_SUCCESS
} from "../actions/types";

const initialState = {
  token: localStorage.getItem("token"),
  isAuthenticated: null,
  loading: false,
  user: null,
  register: false
};

export default function(state = initialState, action) {
  switch (action.type) {
    case REGISTER_SUCCESS:
      return {
        ...state,
        loading: false,
        register: true
      };
    case AUTH_LOADING:
      return {
        ...state,
        loading: true
      };
    case AUTH_SUCCESS:
      localStorage.setItem("token", action.payload.token);
      return {
        ...state,
        token: action.payload.token,
        user: action.payload.user,
        loading: false,
        isAuthenticated: true
      };
    case AUTH_VERIFIED:
      return {
        ...state,
        user: action.payload,
        isAuthenticated: true,
        loading: false
      };
    case LOGOUT_SUCCESS:
    case REGISTER_FAIL:
    case AUTH_FAIL:
      localStorage.removeItem("token");
      return {
        ...state,
        token: null,
        isAuthenticated: null,
        loading: false,
        user: null
      };
    default:
      return state;
  }
}
