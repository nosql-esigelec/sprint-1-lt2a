import React from 'react';
import { Button } from 'primereact/button';

const NavigationButtons = ({ currentSectionNumber, handlePrevSection, handleNextSection, isLastSection, handleRecommendation }) => {
  return (
    <div style={{ display: 'flex', alignItems: 'center' }}>
      {currentSectionNumber > 1 && <Button className="evops-btn" label="Back" onClick={handlePrevSection} type='button' />}
      {!isLastSection && <Button className="evops-btn" label="Next" onClick={handleNextSection} type='button' />}
      {(isLastSection) && <Button className="evops-btn" type="button" onClick={handleRecommendation} label="Get Templates ?" />}
    </div>
  );
};

export default NavigationButtons;