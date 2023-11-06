export const sanitizeProject = async (project) => {
    // Extract only the text fields from the project object
    return Object.entries(project).reduce((acc, [key, value]) => {
      if (Array.isArray(value)) {
        // Check if the array elements are objects containing a 'text' property
        if (value.every(item => item && typeof item === 'object' && 'text' in item)) {
          acc[key] = value.map(item => item.text);
        } else {
          acc[key] = value;
        }
      } else if (value && typeof value === 'object' && 'text' in value) {
        acc[key] = value.text;
      } else {
        acc[key] = value;
      }
      return acc;
    }, {});
  };

  export const validateEmail = (email) => {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
  };
  
  export const validatePassword = (password) => {
    return password.length >= 8;
  };
  
