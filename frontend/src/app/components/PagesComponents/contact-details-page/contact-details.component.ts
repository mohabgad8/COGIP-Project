import { Component, OnInit } from '@angular/core';
import { DetailsComponent } from '../../SmallComponents/details/details.component';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../../service/api.service';

@Component({
  selector: 'app-contact-details',
  imports: [DetailsComponent],
  standalone: true,
  templateUrl: './contact-details.component.html',
  styleUrl: './contact-details.component.css'
})
export class ContactDetailsComponent implements OnInit {

  contactname!: string
  contactData: any = null;
  constructor(private route: ActivatedRoute, private apiService: ApiService) {
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const contactName = params.get('name');
      if (contactName) {
        this.fetchContactData(contactName);

      }
    });
  }
  fetchContactData(contactName: string) {
    this.apiService.fetchData(`get_contact/${contactName}`).subscribe({
      next: (data) => this.contactData = data[0],
      error: (error) => console.error('Erreur lors de la récupération des données contacts', error),
      complete: () => console.log('Données contacts chargées')
    });
  }
}
