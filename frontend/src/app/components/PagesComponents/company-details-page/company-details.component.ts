import {Component, OnInit} from '@angular/core';
import {CompanyInfoComponent} from '../../SmallComponents/company-info/company-info.component';
import {ListComponent} from "../../SmallComponents/list/list.component";
import {ApiService} from "../../../service/api.service";

@Component({
  selector: 'app-company-details-page',
    imports: [
        CompanyInfoComponent,
        ListComponent
    ],
  standalone:true,
  templateUrl: './company-details.component.html',
  styleUrl: './company-details.component.css'
})
export class CompanyDetailsComponent implements OnInit{


    LastFiveInvoicesData: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.apiService.fetchData('get_last_invoices').subscribe((data: any[]) => {
      this.LastFiveInvoicesData = data;
      console.log(data);
    });
}
}
