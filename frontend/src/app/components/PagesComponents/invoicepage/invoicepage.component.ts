import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../../service/api.service';
import {ListComponent} from '../../SmallComponents/list/list.component';

@Component({
  selector: 'app-invoicepage',
  imports: [
    ListComponent
  ],
  standalone: true,
  templateUrl: './invoicepage.component.html',
  styleUrl: './invoicepage.component.css'
})
export class InvoicepageComponent implements OnInit{

  titleInvoices= 'All Invoices'
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

  AllInvoicesData: any[] = []

   constructor(private apiService: ApiService) {
  }
  ngOnInit() {
    this.apiService.getInvoices().subscribe((data: any[]) => {
      this.AllInvoicesData = data;
      console.log(data)
    });
  }



}
