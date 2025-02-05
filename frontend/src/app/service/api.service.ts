import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private apiUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {
  }


  getContact(): Observable<any> {
    return this.http.get<any[]>(`${this.apiUrl}/get_all_contacts`);
  }

   getLastContact(): Observable<any> {
    return this.http.get<any[]>(`${this.apiUrl}/get_last_contacts`);
  }

  getInvoices(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/get_all_invoices`);
  }

  getLastInvoices(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/get_last_invoices`);
  }

  getCompanies(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/get_companies`);
  }

  searchInvoice(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/search_invoice`);
  }


}
