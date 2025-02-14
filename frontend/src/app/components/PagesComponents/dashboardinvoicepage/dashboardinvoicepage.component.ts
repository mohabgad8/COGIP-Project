import { Component, OnInit } from '@angular/core';
import { FormComponent } from '../../SmallComponents/form/form.component';
import { ApiService } from '../../../service/api.service';

interface FormField {
  label: string;
  placeholder?: string;
  type: string;
  options?: string[];
  inputValue?: string;
  selectedOption?: string;
}

@Component({
  selector: 'app-dashboardinvoicepage',
  standalone: true,
  imports: [FormComponent],
  templateUrl: './dashboardinvoicepage.component.html',
  styleUrls: ['./dashboardinvoicepage.component.css']
})
export class DashboardinvoicepageComponent implements OnInit {
  formFields: { invoice: FormField[] } = {
    invoice: [
      { label: 'Date Due', placeholder: 'AAAA-MM-DD', type: 'date', inputValue: '' },
      { label: 'Company Name', placeholder: 'Select a company', type: 'select', options: [], selectedOption: '' }
    ]
  };

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.apiService.fetchData('get_all_companies').subscribe((data: any[]) => {
      const companyField = this.formFields.invoice.find(field => field.label === 'Company Name');
      if (companyField) {
        companyField.options = data.map(company => company.name); 
      }
    });
  }
  

    submitInvoice(formData: any) {
     
      const formattedData = {
        due_date: formData.find((field: any) => field.label === "Date Due")?.value || "",
        company_name: formData.find((field: any) => field.label === "Company Name")?.value || "", 
      };
    
      console.log("📤 Données envoyées au backend:", formattedData);
    
      this.apiService.postData(formattedData, 'add_invoice').subscribe(
        response => console.log('✅ Facture ajoutée avec succès!', response),
        error => console.error('❌ Erreur lors de l\'ajout de la facture:', error)
      );
    }
    
}
