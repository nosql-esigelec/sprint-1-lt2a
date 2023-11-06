// Dropdown.js
import React from 'react';
import { Dropdown } from 'primereact/dropdown';

const DropdownEl = ({ id, label, name, choices, value, defaultVal, optionLabel, onChange }) => (
  
  <div>
         {/* {console.log("Value in DropdownEl", value)}    */}
    <span className="p-float-label">
    <Dropdown 
    key={id}
    name={name}
    value={value} 
    onChange={onChange}
    // onChange={(e) => setSelectedCountry(e.value)} 
    options={choices} 
    optionLabel={optionLabel}
    placeholder={defaultVal} 
    filter 
    className="w-full mb-3"
    />
  <label htmlFor={name} >{label} </label>
  </span>

    {/* <label>{label} </label>
    <select name={name} defaultValue={defaultVal}>
      {choices.map((choice, index) => (
        <option key={index} value={choice}>
          {choice}
        </option>
      ))}
    </select> */}
  </div>
);

export default DropdownEl;
