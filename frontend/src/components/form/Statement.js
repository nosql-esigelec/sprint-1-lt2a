import React from 'react'; 
import { Message } from 'primereact/message';

const Statement = ({ value }) => (
    <div className="card flex justify-content-center">
        <Message text={value} />
    </div>
)

export default Statement;