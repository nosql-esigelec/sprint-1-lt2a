
import React from 'react'; 
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Divider } from 'primereact/divider';
import { InputText } from 'primereact/inputtext';
import { Button } from 'primereact/button';
import { login, getUser } from '../authService';

export default function Login({ onClick}) {
    const [credentials, setCredentials] = useState({
        username: '',
        password: ''
        });
    const [loginStatus, setLoginStatus] = useState(null);
    const navigate = useNavigate();

    const handleChange = (e) => {
        const { name, value } = e.target;
        setCredentials({
          ...credentials,
          [name]: value
        });
      };
    const handleLogin = async () => {
        const response = await login(credentials);
        if (!response.error) {
          const userData = response;
          
        //   const userData = await getUser(token.access_token);
        console.log("The data about user", userData["user"])
        console.log("The data about toekn", userData["access_token"])
        localStorage.setItem('userData', JSON.stringify(userData["user"]));
        localStorage.setItem('token', userData["access_token"]);
        navigate('/projects');
   
        } else {
          setLoginStatus('An error occurred while logging in. Please try again.');
        }
      };
    return (
        <div className="card">
            <div className="flex flex-column md:flex-row">
                <div className="w-full md:w-5 flex flex-column align-items-center justify-content-center gap-3 py-5">
                    <div className="flex flex-wrap justify-content-center align-items-center gap-2">
                        <label className="w-6rem">Username</label>
                        <InputText name="username" value={credentials.username} onChange={handleChange} id="username" type="text" className="w-12rem" />
                    </div>
                    <div className="flex flex-wrap justify-content-center align-items-center gap-2">
                        <label className="w-6rem">Password</label>
                        <InputText name="password" value={credentials.password} onChange={handleChange} id="password" type="password" className="w-12rem" />
                    </div>
                    <Button onClick={handleLogin} label="Login" icon="pi pi-user" className="w-10rem mx-auto"></Button>
                </div>
                <div className="w-full md:w-2">
                    <Divider layout="vertical" className="hidden md:flex">
                        <b>OR</b>
                    </Divider>
                    <Divider layout="horizontal" className="flex md:hidden" align="center">
                        <b>OR</b>
                    </Divider>
                </div>
                <div className="w-full md:w-5 flex align-items-center justify-content-center py-5">
                    <Button onClick={onClick} label="Sign Up" icon="pi pi-user-plus" severity="success" className="w-10rem"></Button>
                </div>
            </div>
        </div>
    )
}
        