{% extends "orders/base.html" %}

{% block title %}
	Pizza Delivery - Home
{% endblock %}

{% block body %}

	<nav class="navbar navbar-expand-lg navbar-light bg-light">
  	<div class="collapse navbar-collapse" id="navbarSupportedContent" style="
  	     background-color: #0C4C7D;
         border-radius: 10px;
         font-family: 'Montserrat', sans-serif;
         padding-left: 25px; padding-right: 25px;">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active" style="background-color: white; border-radius: 10px;">
        <a class="nav-link" href="{% url 'index' %}" >Home</a>
      </li>
     
     <li class="nav-item " style="background-color: white; border-radius: 10px; margin-left: 5px;">
        <a class="nav-link" href="{% url 'show_cart' %}">Cart</a>
      </li>
      <li class="nav-item " style="background-color: white; border-radius: 10px; margin-left: 5px;">
        
        <a class="nav-link" href="{% url 'logout' %}">Logout</a>
      </li>
    </ul>
    <h1>PIZZA</h1>

	</div>
</nav>
<hr>
  <div class="jumbotron">
    <div style="
        background-color: #0C4C7D;
        border-radius: 10px;
        padding: 15px;">
      <h3>Vegetarian Pizzas</h3>

      <table class="table table-sm table-hover">
        <tr><td>  Pizza  </td><td>  Regular  </td><td>  Medium  </td><td>  Large  </td></tr>
        {% for pizza in v_pizzas %}

        <tr><td><a href="{% url 'add_items' pizza.pizza_type pizza.regular pizza.medium pizza.large %}">  {{pizza.pizza_type}}  </a></td><td>  {{pizza.regular}}  </td><td>  {{pizza.medium}}  </td><td>  {{pizza.large}}  </td></tr>

        {% endfor %}
      </table>

    </div>

    <div style="
        background-color: #0C4C7D;
        border-radius: 10px;
        padding: 15px;
        margin-top: 10px;">
      <h3>Non-Vegetarian Pizzas</h3>
      <table class="table table-sm table-hover">
        <tr><td>  Pizza  </td><td>  Regular  </td><td>  Medium  </td><td>  Large  </td></tr>
        {% for pizza in n_pizzas %}

        <tr><td><a href="{% url 'add_items' pizza.pizza_type pizza.regular pizza.medium pizza.large %}">  {{pizza.pizza_type}}  </a></td><td>  {{pizza.regular}}  </td><td>  {{pizza.medium}}  </td><td>  {{pizza.large}}  </td></tr>

        {% endfor %}
      </table>

    </div>

    <div style="
        background-color: #0C4C7D;
        border-radius: 10px;
        padding: 15px;
        margin-top: 10px;
        margin-bottom: -100px">
      <h3>Toppings</h3>
      <table class="table table-sm table-hover">
        {% for t in toppings %}
        <tr><td>{{t.name}}</td><td>{{t.price}}</td> </tr>
        {% endfor %}
      </table>

    </div>

    
  </div>


{% endblock %}
