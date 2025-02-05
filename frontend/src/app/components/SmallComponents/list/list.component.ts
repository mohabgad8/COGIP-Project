import { Component, Input } from '@angular/core';
import {NgForOf, NgIf} from '@angular/common';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-list',
  standalone: true,
  templateUrl: './list.component.html',
  imports: [
    NgIf,
    FormsModule,
    NgForOf
  ],
  styleUrls: ['./list.component.css']
})
export class ListComponent {
  @Input() showSearchBar: boolean = false;
  @Input() showPagination: boolean= true
  @Input() column: any[] = [];
  @Input() data: any[] = [];
  @Input() title: string = '';
  @Input() itemsPerPage: number = 10;

  searchTerm: string = '';
  currentPage: number = 1;


    formatDate(date: any): string {
    const d = new Date(date);
    return d.toLocaleDateString('fr-FR');

  }
  get filteredData() {
    let filtered = this.data;

    if (this.searchTerm) {
      filtered = this.data.filter(row =>
        this.column.some(col =>
          row[col.key]?.toString().toLowerCase().includes(this.searchTerm.toLowerCase())
        )
      );
    }

    return filtered.slice((this.currentPage - 1) * this.itemsPerPage, this.currentPage * this.itemsPerPage);
  }

  totalPages(): number {
    return Math.ceil(this.data.length / this.itemsPerPage);
  }

  goToPage(page: number) {
    this.currentPage = page;
  }
}
