//for tag selection
import React, { useState } from "react";
import { Chips } from "primereact/chips";
const ChipsEl = ({ id, label, name, defaultVal, value, onChange }) => {

    return (
        <div>
            <span className="p-float-label">
            <Chips 
                key={id}
                name={name}
                value={value} 
                onChange={onChange} 
                className="w-full mb-3"
                placeholder={defaultVal}/>
                 <label htmlFor={name} >{label} </label>
                 </span>
        </div>
        );
  };
  
  export default ChipsEl;
  
