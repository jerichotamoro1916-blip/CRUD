import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './app.html',
})
export class AppComponent {
  apiUrl = 'http://127.0.0.1:8000/products';

  title = '';
  price: number | null = null;
  count: number | null = null;

  products: any[] = [];

  constructor(private http: HttpClient) {
    this.loadProducts();
  }

  loadProducts(): void {
    this.http.get<any[]>(this.apiUrl).subscribe(data => {
      this.products = data;
    });
  }

  createProduct(): void {
  if (!this.title || this.price === null || this.count === null) {
    return;
  }

  const product = {
    title: this.title,
    price: this.price,
    count: this.count
  };

  this.http.post(this.apiUrl, product).subscribe(() => {
    this.loadProducts();

    // reset form
    this.title = '';
    this.price = null;
    this.count = null;
  });
}


  deleteProduct(id: number): void {
    this.http.delete(`${this.apiUrl}/${id}`).subscribe(() => {
      this.loadProducts();
    });
  }
}
