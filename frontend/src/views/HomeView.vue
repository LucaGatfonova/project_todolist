<template>
 <div class="container">
	<Navbar/>
	  <section class="vh-100">
		<div class="container py-5 h-100">
		  <div class="row d-flex justify-content-center align-items-center h-100">
			<div class="col">
			  <div class="card" id="list1" style="border-radius: .75rem; background-color: #eff1f2;">
				<div class="card-body py-4 px-4 px-md-5">

				  <div class="pb-2">
					<b-navbar toggleable="sm" type="light" variant="light">
					  <b-navbar-toggle target="nav-text-collapse"></b-navbar-toggle>

						<b-collapse id="nav-text-collapse" is-nav>
							<b-navbar-nav class="form" v-on:submit.prevent="addTodo">
								<div class="todo"><b-form-input v-model="description" id="input-large" size="lg" placeholder="Enter your todo"></b-form-input></div>
								<div class="todo"><b-form-datepicker id="datepicker-lg" size="lg" type="date" v-model="date" :min="new Date().toISOString().slice(0, 10)"></b-form-datepicker></div>
								<div class="todo"><b-button v-on:click="addTodo" variant="dark">Add todo</b-button></div>
							</b-navbar-nav>
					    </b-collapse>
					  </b-navbar>
				  </div>

				<hr class="my-4">
				<h2>
					<span>Todo</span>
				</h2>

				  <ul class="list-group list-group-horizontal rounded-0 bg-transparent" v-if="todo.status === false" v-for="todo in todos" v-bind:key="todo.id">
					<li
						class="list-group-item d-flex align-items-center ps-0 pe-3 py-1 rounded-0 border-0 bg-transparent">
						<div class="form-check">
						<input class="form-check-input me-0" type="checkbox" id="flexCheckChecked1"
						@click="setStatus(todo.id, true)" />
						</div>
					</li>
					<li
						class="list-group-item px-3 py-1 d-flex align-items-center flex-grow-1 border-0 bg-transparent">
						<p class="lead fw-normal mb-0">{{ todo.description }}</p>
					</li>
					<li class="list-group-item ps-3 pe-0 py-1 rounded-0 border-0 bg-transparent">
						<div class="d-flex flex-row justify-content-end mb-1">
							<b-button class="dark" v-on:click="deleteTodo(todo.id)">
								<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16" data-darkreader-inline-fill="" style="--darkreader-inline-fill:currentColor;">
									<path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"></path>
									<path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"></path>
								</svg>
							</b-button>
						</div>
						<div class="text-end text-muted">
							<p class="small mb-0"><i class="fas fa-info-circle me-2"></i>{{ todo.date }}</p>
						</div>
					</li>
				  </ul>
				<h2>
					<span>Done</span>
				</h2>

				  <ul class="list-group list-group-horizontal rounded-0 bg-transparent" v-if="todo.status === true" v-for="todo in todos" v-bind:key="todo.id">
					<li
						class="list-group-item d-flex align-items-center ps-0 pe-3 py-1 rounded-0 border-0 bg-transparent">
						<div class="form-check">
						<input class="form-check-input me-0" type="checkbox" id="flexCheckChecked1" checked 
						@click="setStatus(todo.id, false)"/>
						</div>
					</li>
					<li
						class="list-group-item px-3 py-1 d-flex align-items-center flex-grow-1 border-0 bg-transparent">
						<p class="lead fw-normal mb-0">{{ todo.description }}</p>
					</li>
					<li class="list-group-item ps-3 pe-0 py-1 rounded-0 border-0 bg-transparent">
						<div class="d-flex flex-row justify-content-end mb-1">
							<b-button class="dark" v-on:click="deleteTodo(todo.id)">
								<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16" data-darkreader-inline-fill="" style="--darkreader-inline-fill:currentColor;">
									<path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"></path>
									<path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"></path>
								</svg>
							</b-button>
						</div>
						<div class="text-end text-muted">
							<p class="small mb-0"><i class="fas fa-info-circle me-2"></i>{{ todo.date }}</p>
						</div>
					</li>
				  </ul>
				</div>
			  </div>
			</div>
		  </div>
		</div>
	  </section>
 </div>
</template>
  
<script>
import axios from 'axios';
import Navbar from "@/components/Navbar.vue";

const API_URL = 'http://127.0.0.1:8000/'

let today = new Date().toISOString().slice(0, 10)

export default {
	components: { 
	  Navbar,
	},	
	data () {
		return {
			todos: [],
			description: '',
			date: today,
			status: false
		}
	},
	mounted () {
		this.getTodo()
	},
	methods: {
		getTodo(){
			axios.get('http://127.0.0.1:8000/todos/')
			.then(response => this.todos = response.data)
		},
		addTodo() {
			axios({
				method: 'post',
				url: API_URL + 'todos/',
				data: {
					description: this.description,
					date: this.date,
					status: this.status
				}
			}).then((response) => {
				let newTodo = {
				'id': response.data.id,
				'description': this.description,
				'date': this.date,
				'status': this.status
			}
			this.todos.push(newTodo)
			this.description = ''
			this.date = ''
			this.status = false
		 }).catch((error) => {
			console.log(error)
		 })
		},
		setStatus(todo_id, status) {
			const todo = this.todos.filter(todo => todo.id === todo_id)[0]
			const description = todo.description
			const date = todo.date

			axios({
				method: 'put',
				url: API_URL + 'todos/' + todo_id + '/',
				headers: {
					'Content-Type': 'application/json',
				},
				data: {
					status: status,
					description: description,
					date: date
				},
			}).then(() => {
				todo.status = status
			})
		},
		deleteTodo(id) {
			axios.delete(`http://127.0.0.1:8000/todos/${id}`)
			.then(() => {
				let index = this.todos.map(todos => todos.id).indexOf(id);
				this.todos.splice(index, 1)
			}).catch(error => {
				console.log(error)
			})
		},
	},
};

</script>

<style lang="scss">

body {
  font-family: 'Ubuntu', sans-serif;
  font-weight: 300;
}
.todo {
  justify-content: space-between;
  margin: 25px 0;
  padding-right: 20px;
}

</style>