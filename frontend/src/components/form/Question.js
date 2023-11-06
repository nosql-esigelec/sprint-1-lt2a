import React from 'react';
import DropdownEl from './Dropdown';
import ChipsEl from './Chips';
import MultiSelectEl from './MultiSelect';
import TextInput from './TextInput';
import TextAreaEl from './TextArea';
import SwitchEl from './Switch';
import Statement from './Statement';

const Question = ({ id, type, label, name, value, choices, optionLabel, onChange, placeholder, ...otherProps }) => {
  // console.log("Props in Question:", {type, label, name, value, choices, onChange, placeholder});

  switch(type) {
    case 'text':
      // console.log("Question type is text")
      return (
        <TextInput
          id={id}
          key={id}
          label={label}
          name={name}
          placeholder={placeholder}
          value={value}
          onChange={onChange}
        />
      );

    case 'select':
      // console.log("Question type is select")
      return (
        <DropdownEl
          id={id}
          key={id}
          label={label}
          name={name}
          defaultVal={placeholder}
          value={value}
          choices={choices}
          optionLabel={optionLabel}
          onChange={onChange}
          
        />
      );

    case 'multiselect':
      // console.log("Question type is multiSelect")
      return (
        <MultiSelectEl
          id={id}
          key={id}
          label={label}
          name={name}
          optionLabel={optionLabel}
          defaultVal={placeholder}
          value={value}
          choices={choices}
          onChange={onChange}
          {...otherProps}
        />
      );

    case 'chips':
      // console.log("Question type is chips")
      return (
        <ChipsEl
          id={id}
          label={label}
          type="text"
          name={name}
          placeholder={placeholder}
          value={value}
          onChange={onChange}
        />
      );
      case 'textarea': // New case for textarea
      return (
        <TextAreaEl
          id={id}
          label={label}
          name={name}
          placeholder={placeholder}
          value={value}
          onChange={onChange}
        />
      );

    case 'switch': // New case for switch
      return (
        <SwitchEl
          id={id}
          label={label}
          name={name}
          value={value}
          onChange={onChange}
        />
      );
      case 'switch': // New case for switch
      return (
        <Statement
          id={id}
          label={label}
          name={name}
          value={value}
          onChange={onChange}
        />
      );
    default:
      return null;
  }
};

export default Question;
