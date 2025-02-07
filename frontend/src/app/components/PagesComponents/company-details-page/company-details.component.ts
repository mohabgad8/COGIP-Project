import {Component, OnInit} from '@angular/core';
import {ListComponent} from "../../SmallComponents/list/list.component";
import {ApiService} from "../../../service/api.service";
import {ActivatedRoute} from '@angular/router';
import {DetailsComponent} from '../../SmallComponents/details/details.component';

@Component({
  selector: 'app-company-details-page',
    imports: [
        DetailsComponent,
        ListComponent
    ],
  standalone:true,
  templateUrl: './company-details.component.html',
  styleUrl: './company-details.component.css'
})
export class CompanyDetailsComponent implements OnInit{

   companyName!: string
   invoices: any[] = []
   companyData: any = null;
   columns= [
    { key: 'ref', label: 'Invoice Number' },
    { key: 'date_due', label: 'Dates' },
    { key: 'company_name', label: 'Company'},
    { key: 'created_at', label: 'Created At'}
  ]


 constructor(private route: ActivatedRoute, private apiService: ApiService) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const companyName = params.get('companyName');
      if (companyName) {
        this.fetchCompanyData(companyName);
        this.fetchInvoices(companyName);
      }
    });
  }

  fetchCompanyData(companyName: string) {
    this.apiService.fetchData(`get_company/${companyName}`).subscribe({
      next: (data) => this.companyData = data[0],
      error: (error) => console.error('Erreur lors de la récupération des données entreprise', error),
      complete: () => console.log('Données entreprise chargées')
    });
  }

  fetchInvoices(companyName: string) {
    this.apiService.fetchData(`get_last_invoices_company/${companyName}`).subscribe({
      next: (data) => this.invoices = data,
      error: (error) => console.error('Erreur lors de la récupération des factures', error),
      complete: () => console.log('Factures chargées')
    });
  }
}

