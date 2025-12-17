import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './app.html',
})
export class AppComponent implements OnInit {

  apiUrl = 'http://127.0.0.1:8000/products';

  // form fields
  title = '';
  price: number | null = null;
  count: number | null = null;

  // edit mode
  editingId: number | null = null;

  // data
  products: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.loadProducts();
  }

  loadProducts() {
    this.http.get<any[]>(this.apiUrl).subscribe(data => {
      this.products = data;
    });
  }

  createProduct() {
  if (!this.title || this.price === null || this.count === null) return;

  const product = {
    title: this.title,
    price: this.price,
    count: this.count
  };

  this.http.post<any>(this.apiUrl, product).subscribe(created => {
    this.products.unshift(created);
    this.resetForm();
  });
}


  editProduct(product: any) {
    this.editingId = product.id;
    this.title = product.title;
    this.price = product.price;
    this.count = product.count;
  }

  updateProduct() {
  if (this.editingId === null) return;

  const product = {
    title: this.title,
    price: this.price,
    count: this.count
  };

  const index = this.products.findIndex(p => p.id === this.editingId);

  this.http.put<any>(`${this.apiUrl}/${this.editingId}`, product)
    .subscribe(updated => {
      this.products[index] = updated;
      this.resetForm();
    });
}


  deleteProduct(id: number) {
  // 🔥 remove immediately
  this.products = this.products.filter(p => p.id !== id);

  this.http.delete(`${this.apiUrl}/${id}`).subscribe({
    error: () => {
    }
  });
}

  trackById(index: number, product: any) {
    return product.id;
}

  resetForm() {
    this.title = '';
    this.price = null;
    this.count = null;
    this.editingId = null;
  }
}

