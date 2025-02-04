import { Component, OnInit } from '@angular/core';
import {BannerComponent} from '../SmallComponents/banner/banner.component';
import {ListComponent} from '../SmallComponents/list/list.component';
import {InfoComponent} from '../SmallComponents/info/info.component';
import {ApiService} from '../../service/api.service';


@Component({
  selector: 'app-homepage',
  imports: [BannerComponent, ListComponent, InfoComponent],
  standalone: true,
  templateUrl: './homepage.component.html',
  styleUrl: './homepage.component.css'
})

export class HomepageComponent implements OnInit {
  titleInvoices= 'Last Invoices'
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
      key: "created_at", label: "Created at"
    }]

  lastInvoicesData: any[] = []

  titleContact= 'Last Contacts'
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

  lastContactData: any[] = []

  titleCompanies= 'Last Companies'
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
      key: "created_at", label: "Created at"
    }
  ]
  lastCompaniesData: any[] = []

  constructor(private apiService: ApiService) {
  }

  ngOnInit() {
    this.apiService.getContact().subscribe((data: any[]) => {
      this.lastContactData = data;
      console.log(data)
    });


    this.apiService.getInvoices().subscribe((data: any[]) => {
      this.lastInvoicesData = data;
      console.log(data)
    });

    this.apiService.getCompanies().subscribe((data: any[]) => {
      this.lastCompaniesData = data;
      console.log(data)
    });
  }
}
