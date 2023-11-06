// Dropdown.js
import React from 'react';
import { MultiSelect } from 'primereact/multiselect';

const MultiSelectEl = ({ id, label, name, choices, value, defaultVal, onChange, optionLabel,maxSelectedLabels }) => (
  <div>
    <span className="p-float-label">
      {console.log("Key in MultiSelectEl", id)}
    <MultiSelect 
    key={id}
    name={name}
    value={value} 
    onChange={onChange}
    display="chip" 
    options={choices} 
    maxSelectedLabels={maxSelectedLabels}
    optionLabel={optionLabel}
    placeholder={defaultVal} 
    filter 
    className="w-full mb-3" />
  <label htmlFor={name} >{label} </label>
  </span>

  </div>
);

export default MultiSelectEl;

