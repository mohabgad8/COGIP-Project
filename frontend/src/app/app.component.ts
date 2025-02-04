import { Component } from '@angular/core';
import {RouterOutlet} from '@angular/router';
import {HeaderComponent} from './components/SmallComponents/header/header.component';
import {FooterComponent} from './components/SmallComponents/footer/footer.component';



@Component({
  selector: 'app-root',
  standalone:true,
  imports: [HeaderComponent, FooterComponent, RouterOutlet],
  templateUrl:'app.component.html',
  styleUrl: 'app.component.css'
})
export class AppComponent {}

  contactsColumn = [
    {
      key: "name", label: "Name"
    },
    {
      key: "phone", label: "Phone"
    },
    {
      key: "mail", label: "Mail"
    },
    {
      key: "company", label: "Company"
    },
    {
      key: "create at", label: "Create at"
    }
  ]

