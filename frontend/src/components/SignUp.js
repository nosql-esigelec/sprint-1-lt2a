import React, { useState, useRef } from 'react';
import { Divider } from 'primereact/divider';
import { InputText } from 'primereact/inputtext';
import { Button } from 'primereact/button';
import { Toast } from 'primereact/toast';
import { validateEmail, validatePassword } from '../utils/helpers';
import { Messages } from 'primereact/messages'
import { Message } from 'primereact/message';
import { signup } from '../authService';
export default function Signup({onClick}) {
    const [userData, setUserData] = useState({
        username: '',
        password: '',
        email: ''
      });
      const toast = useRef(null);
      const [signupStatus, setSignupStatus] = useState(null);
      const [emailValid, setEmailValid] = useState(true);
      const [passwordValid, setPasswordValid] = useState(true);
      
      const handleChange = (e) => {
        const { name, value } = e.target;
        setUserData({
          ...userData,
          [name]: value
        });
      };
    
      const handleSignup = async () => {

        setEmailValid(true);
        setPasswordValid(true);

        if (!validateEmail(userData.email)) {
            setEmailValid(false);
            return;
          }
        if (!validatePassword(userData.password)) {
            setPasswordValid(false);
           
            return;
          }

        const response = await signup(userData);
        if (!response.error) {
          const message = `Welcome ${userData.username}! Login and get started!`;
          toast.current.show({severity:'success', summary: 'Success', detail: message, life: 3000});
          setTimeout(() => {
            onClick();
          }, 2000)

          
        } else {
          setSignupStatus('An error occurred while signing up. Please try again.');
        }
      };
    
    return (
        <div className="card">
            <Toast ref={toast} />
            <div className="flex flex-column md:flex-row">
                <div className="w-full md:w-5 flex flex-column align-items-center justify-content-center gap-3 py-5">
                    <div className="flex flex-wrap justify-content-center align-items-center gap-2">
                        <label className="w-6rem">Username</label>
                        <InputText name="username" value={userData.username} onChange={handleChange} id="username" type="text" className="w-12rem" />
                    </div>
                    <div className="flex flex-wrap justify-content-center align-items-center gap-2">
                        <label className="w-6rem">Email</label>
                        <InputText name="email" value={userData.email} onChange={handleChange} id="email" type="email" className="w-12rem" />
                        {!emailValid && <Message severity="error" text="Please enter a valid email address." />}
                        
                    </div>
                    <div className="flex flex-wrap justify-content-center align-items-center gap-2">
                        <label className="w-6rem">Password</label>
                        <InputText name="password" value={userData.password} onChange={handleChange} id="password" type="password" className="w-12rem" />
                        {!passwordValid && <Message severity="error" text="At least 8 characters long." />}
                    </div>
                    <div className="flex flex-wrap justify-content-center align-items-center gap-2">
                        <label className="w-6rem">Confirm Password</label>
                        <InputText id="confirmPassword" type="password" className="w-12rem" />
                    </div>
                    <Button label="Sign Up" icon="pi pi-user-plus" onClick={handleSignup} className="w-10rem mx-auto"></Button>
                    
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
                    <Button onClick={onClick} label="Login" icon="pi pi-user" severity="success" className="w-10rem"></Button>
                </div>
            </div>
        </div>
    )
}
