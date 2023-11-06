// Switch.js
import React from "react";
import { InputSwitch } from "primereact/inputswitch";


const SwitchEl = ({ id, label, name, value, onChange }) => {

  return (
  <div>

            <span className="flex flex-column">
            <label htmlFor={name} >{label}  </label>
            <br></br>
                <InputSwitch 
                  autoResize
                  key={id}
                  id={name} 
                  name={name}
                  checked={value} 
                  onChange={onChange} 
                  className="mb-3"/>
                
            </span>
  

  </div>);
};

export default SwitchEl;

