// TextInput.js
import React from "react";
import { InputText } from 'primereact/inputtext';


const TextInput = ({ id, label, name, defaultVal, value, onChange }) => {

  return (
  <div>

            <span className="p-float-label">
                <InputText 
                  key={id}
                  id={name} 
                  name={name}
                  value={value} 
                  onChange={onChange} 
                  placeholder={defaultVal} 
                  className="w-full mb-3"/>
                <label htmlFor={name} >{label} </label>
            </span>
  

  </div>);
};

export default TextInput;

