import React, { useState } from 'react';
//import { useRouter } from 'next/router';
import { Toolbar } from 'primereact/toolbar';
import { Button } from 'primereact/button';
import { Menu } from 'primereact/menu';
import { Sidebar } from 'primereact/sidebar';
import { Avatar } from 'primereact/avatar';
import '../../styles/Menu.css';


export default function NavBar({onNewAction, actionLabel}) {
    //const router = useRouter();
    let items = [
        {label: 'Projects', icon: 'pi pi-fw pi-folder-open', url: "/projects"},
        {label: 'Templates', icon: 'pi pi-fw pi-clone', url:"/templates"},

    ];
    const [visible, setVisible] = useState(false);
    const username = JSON.parse(localStorage.getItem('userData')).username;
    const capitalize = (s) => {
        if (typeof s !== 'string') return ''
        return s.charAt(0).toUpperCase() + s.slice(1);
      }
    
    const avatar = (s) => {
    if (typeof s !== 'string') return ''
    return s.charAt(0).toUpperCase() ;
    }
    const startContent = (
        <React.Fragment>
            <Button icon="pi pi-bars" onClick={() => setVisible(true)} className="mr-2" />

            
        </React.Fragment>
    );

    const endContent = (
        <React.Fragment>
            <Button label={actionLabel} icon="pi pi-plus" className="p-button-success mr-2" onClick={onNewAction} />
        </React.Fragment>
    );

    return (
        <div className="card">
            <Toolbar start={startContent} end={endContent} />
            <Sidebar visible={visible} onHide={() => setVisible(false)}>
            <Avatar label={avatar(username)} className="mr-2" size="large" />
            Welcome, {capitalize(username)}!
            <Menu model={items} />
            </Sidebar>        
        </div>
    );
}
        