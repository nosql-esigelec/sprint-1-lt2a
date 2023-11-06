import React, { useState } from 'react';
import Login from '../components/Login';
import Signup from '../components/SignUp';

const Home = () => {
  const [showLogin, setShowLogin] = useState(false);
  const [showSignup, setShowSignup] = useState(true);

  const toggleComponents = () => {
    setShowLogin(!showLogin);
    setShowSignup(!showSignup);
  };

  return (
    <div className="p-grid p-justify-center align-items-center auth-container">
      <div className="p-col-8">
  
          <div className="flex align-items-center justify-content-center">
    <div className="surface-card p-4 shadow-2 border-round w-full lg:w-6">
        <div className="text-center mb-5">
            <img src="logo512.png" alt="hyper" height={100} className="mb-3" />
            <div className="text-900 text-3xl font-medium mb-3">Welcome Back to GoCod!</div>
            <span className="text-600 font-medium line-height-3">Don't have an account?</span>
            <span className="font-medium no-underline ml-2 text-blue-500">Create today!</span>
            <p>Let's empower your team with the tool you want to create and manage your dev projects!  </p>
        </div>
        {showLogin && <Login onClick={toggleComponents}/>}
          {showSignup && <Signup onClick={toggleComponents}/>}

    </div>
</div>
     


      </div>
    </div>
  );
};

export default Home;



