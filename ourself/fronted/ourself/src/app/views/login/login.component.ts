import { Component } from '@angular/core';

import { FormGroup, FormControl, Validators } from '@angular/forms';
import { UserService } from '../../service/api/user.service';
import { LoginI } from '../../models/login/login.interface';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  loginForm = new FormGroup({
    user: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required)
  })

  constructor(private userService:UserService){}

  onLogin(){
    // let users:LoginI = {
    //   user: this.loginForm.get('user')?.value,
    //   password: this.loginForm.get('password')?.value
    // }

    const form:any = this.loginForm.value
    this.userService.loginByEmail(form).subscribe(data => {
      console.log(data);
    });
  }

}
