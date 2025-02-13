import { Component } from '@angular/core';
import { FormComponent } from '../../SmallComponents/form/form.component';
import {ApiService} from '../../../service/api.service';

@Component({
  selector: 'app-dashboardinvoicepage',
  standalone: true,
  imports: [FormComponent],
  templateUrl: './dashboardinvoicepage.component.html',
  styleUrls: ['./dashboardinvoicepage.component.css']
})
export class DashboardinvoicepageComponent {
  formFields = {
    invoice: [
      { label: 'Date Due', placeholder: 'AAAA-MM-DD', type: 'date' },
      { label: 'Company Name', placeholder: 'Ex: Raviga', type: 'text' }
    ]
  };

  constructor(private apiService: ApiService) {}

  submitInvoice(formData: any) {
    this.apiService.postData(formData, 'add_invoice').subscribe(response => {
      console.log('Invoice created successfully!', response);
    });
  }
}
