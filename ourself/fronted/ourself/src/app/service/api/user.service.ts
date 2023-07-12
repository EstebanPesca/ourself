import { Injectable } from '@angular/core';
import { LoginI } from '../../models/login/login.interface';
import { ResponseI } from '../../models/login/response.interface';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  urlApi:string = "http://127.0.0.1:8000/";

  constructor( private http:HttpClient) { }

  loginByEmail(form:LoginI):Observable<ResponseI>{

    let path = this.urlApi + "users/users";

    return this.http.post<ResponseI>(path, form);
  }

}
