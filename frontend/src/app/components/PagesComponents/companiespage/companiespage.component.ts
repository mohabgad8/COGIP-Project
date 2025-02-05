import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../../service/api.service';
import {ListComponent} from '../../SmallComponents/list/list.component';


@Component({
  selector: 'app-companiespage',
  imports: [ListComponent],
  standalone:true,
  templateUrl: './companiespage.component.html',
  styleUrl: './companiespage.component.css'
})
export class CompaniespageComponent implements OnInit {

  titleCompanies = 'All Companies'
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
  AllCompaniesData: any[] = []

  constructor(private apiService: ApiService) {
  }

  ngOnInit() {
    this.apiService.getCompanies().subscribe((data: any[]) => {
        this.AllCompaniesData = data;
        console.log(data)
      }
    )
  }
}
