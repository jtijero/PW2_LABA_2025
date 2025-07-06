import { Component } from '@angular/core';
import { Product } from '../../services/products';
import { Products } from '../../services/products';
@Component({
  selector: 'app-products',
  imports: [],
  templateUrl: './products.html',
  styleUrl: './products.css'
})
export class Productos {
  productos : Product[] = [];
  constructor(private product:Products){ //esto es export class Products { de services
    this.productos = this.product.getproducts();
  }
}
