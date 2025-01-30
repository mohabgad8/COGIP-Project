import { Component } from '@angular/core';
import {HeaderComponent} from './components/header/header.component';
import {ListComponent} from './components/list/list.component';


@Component({
  selector: 'app-root',
  standalone:true,
  imports: [HeaderComponent, ListComponent],
  templateUrl:'app.component.html',
  styleUrl: 'app.component.css'
})
export class AppComponent {

  invoiceColumn = [
    {
      key: "invoice number", label: "Invoice number"
    },
    {
      key: "dates due", label: "Dates due"
    },
    {
      key: "company", label: "Company"
    },
    {
      key: "create at", label: "Created at"
    }]

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

  companiesColumn = [
    {
      key: "name", label: "Name"
    },
    {
      key: "tva", label: "TVA"
    },
    {
      key: "country", label: "Country"
    },
    {
      key: "type", label: "Type"
    },
    {
      key: "create at", label: "Create at"
    }
  ]

}
