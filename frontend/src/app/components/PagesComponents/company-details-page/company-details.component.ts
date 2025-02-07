import {Component, OnInit} from '@angular/core';
import {CompanyInfoComponent} from '../../SmallComponents/company-info/company-info.component';
import {ListComponent} from "../../SmallComponents/list/list.component";
import {ApiService} from "../../../service/api.service";
import {ActivatedRoute} from '@angular/router';

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

   companyName!: string
   invoices: any[] = []
   columns= [
    { key: 'ref', label: 'Invoice Number' },
    { key: 'dates_due', label: 'Dates' },
    { key: 'name', label: 'Company'},
    { key: 'created_at', label: 'Created At'}
  ]


  constructor(private apiService: ApiService, private route: ActivatedRoute) {}
 ngOnInit():void{

  this.route.paramMap.subscribe(params => {
    this.companyName = params.get('company_name') || '';

    if(this.companyName) {
    this.apiService.fetchData(`get_last_invoices_company/${this.companyName}`).subscribe((data:any[]) => {
      this.invoices = data
      });
    }
  });
}

}

