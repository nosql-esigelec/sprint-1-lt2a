// TextArea.js
import React from "react";
import { InputTextarea } from "primereact/inputtextarea";


const TextAreaEl = ({ id, label, name, defaultVal, value, onChange }) => {

  return (
  <div>

            <span className="p-float-label">
                <InputTextarea 
                  autoResize
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

export default TextAreaEl;

