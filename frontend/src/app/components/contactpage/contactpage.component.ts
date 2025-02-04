import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../service/api.service';
import {ListComponent} from '../SmallComponents/list/list.component';

@Component({
  selector: 'app-contactpage',
  imports: [
    ListComponent
  ],
  standalone:true,
  templateUrl: './contactpage.component.html',
  styleUrl: './contactpage.component.css'
})
export class ContactpageComponent implements OnInit{

   titleContacts= 'All Contacts'
  contactsColumn = [
    {
      key: "name", label: "Name"
    },
    {
      key: "phone", label: "Phone"
    },
    {
      key: "email", label: "Mail"
    },
    {
      key: "company", label: "Company"
    },
    {
      key: "create at", label: "Created at"
    }
  ]

  AllContactsData: any[] = []

   constructor(private apiService: ApiService) {
  }
  ngOnInit() {
    this.apiService.getContact().subscribe((data: any[]) => {
      this.AllContactsData = data;
      console.log(data)
    });
  }

}
