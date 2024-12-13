import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/api/";
const LOGIN_URL = `${BASE_URL}token/`;
const REFRESH_URL = `${BASE_URL}token/refresh/`;
const LOGOUT_URL = `${BASE_URL}logout/`;
const AUTH_URL = `${BASE_URL}authenticated/`;
const UPLOAD_URL = "http://127.0.0.1:8000/preprocess/";

export const login = async (username, password) => {
  const response = await axios.post(
    LOGIN_URL,
    {
      username: username,
      password: password,
    },
    { withCredentials: true }
  );

  return response.data.success;
};

export const refreshToken = async () => {
  try {
    await axios.post(REFRESH_URL, {}, { withCredentials: true });
    return true;
  } catch (error) {
    return false;
  }
};

// const call_refresh = async (error, func) => {
//     if (error.response && error.response.status === 401) {
//         const tokenRefreshed = await refreshToken();

//         if (tokenRefreshed) {
//             const retryReponse = await func();
//             return retryReponse.data;
//         }
//     }

//     return false;
// }

export const logout = async () => {
  try {
    await axios.post(LOGOUT_URL, {}, { withCredentials: true });
    return true;
  } catch (error) {
    return false;
  }
};

export const is_authenticated = async () => {
  try {
    await axios.post(AUTH_URL, {}, { withCredentials: true });
    return true;
  } catch (error) {
    return false;
  }
};

export const preprocess = async (file) => {
  try {
    const formData = new FormData();
    formData.append('file', file);

    // Upload the file to the backend
    const response = await axios.post(UPLOAD_URL, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error('Upload failed:', error.response?.data || error.message);
    alert('An error occurred during upload or analysis.');
  }
}