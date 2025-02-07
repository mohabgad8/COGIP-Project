import { Component, OnInit } from '@angular/core';
import {BannerComponent} from '../../SmallComponents/banner/banner.component';
import {ListComponent} from '../../SmallComponents/list/list.component';
import {InfoComponent} from '../../SmallComponents/info/info.component';
import {ApiService} from '../../../service/api.service';




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
      key: "ref", label: "Invoice number"
    },
    {
      key: "date_due", label: "Dates due"
    },
    {
      key: "name", label: "Company"
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
      key: "company_name", label: "Company"
    },
    {
      key: "created_at", label: "Created at"
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
    this.apiService.fetchData('get_last_contacts').subscribe((data: any[]) => {
      this.lastContactData = data;
      console.log(data)
    });



    this.apiService.fetchData('get_last_invoices').subscribe((data: any[]) => {
      this.lastInvoicesData = data;
      console.log(data)
    });

    this.apiService.fetchData('get_last5_companies').subscribe((data: any[]) => {
      this.lastCompaniesData = data;
      console.log(data)
    });
  }
}
