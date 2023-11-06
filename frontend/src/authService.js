import apiClient from './api'; // Import your apiClient

export const signup = async (userData) => {
  // return userData
  try {
    console.log('Signup', userData);
    apiClient.defaults.headers['Content-Type'] = 'application/json';
    const response = await apiClient.post('/users/register', userData);
    console.log('Signup', response);
    return response.data;
  } catch (error) {
    console.error('An error occurred while signing up: ', error);
    return { error: 'An error occurred while signing up.' };
  }
};

export const login = async (credentials) => {
  // return credentials
  try {
    const payload = {
      grant_type: '',
      username: credentials.username,
      password: credentials.password,
      scope: '',
      client_id: '',
      client_secret: ''
    };
    apiClient.defaults.headers['Content-Type'] = 'application/x-www-form-urlencoded';
    const response = await apiClient.post('/users/login', payload);
    console.log('Login', response);
    return response.data;
  } catch (error) {
    console.error('An error occurred while logging in: ', error);
    return { error: 'An error occurred while logging in.' };
  }
};

export const logout = async () => {
  try {
    apiClient.defaults.headers['Content-Type'] = 'application/json';
    const response = await apiClient.post('/users/logout');
    
    console.log('Logout', response);
    return response.data;
  } catch (error) {
    console.error('An error occurred while logging out: ', error);
    return { error: 'An error occurred while logging out.' };
  }
};


export const checkUser = async (token) => {
  try {
    apiClient.defaults.headers['Content-Type'] = 'application/json';
    const response = await apiClient.get('/users/verify', token);
    console.log('Check User', response);
    return response.data;
  } catch (error) {
    console.error('An error occurred while signing up: ', error);
    return { error: 'An error occurred while signing up.' };
  }
};

export const getUser = async (username) => {
  try {
    console.log('Get User', username);
    apiClient.defaults.headers['Content-Type'] = 'application/json';
    const payload = {
      username: username
    };
    const response = await apiClient.get('/users', 
    {params: payload}
    );
    console.log('Get User', response);
    return response.data;
  } catch (error) {
    console.error('An error occurred while signing up: ', error);
    return { error: 'An error occurred while signing up.' };
  }
};

export const getUserId = async () => {
  const user = JSON.parse(localStorage.getItem('userData'));
  const userData = await getUser(user.username)
  return user ? userData.uid : null;
}