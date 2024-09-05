body {
            font-family: 'Open Sans', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        
        .container {
            max-width: 600px;
            margin: 40px auto;
            padding: 20px;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            color: #333;
            font-weight: 600;
            margin-bottom: 20px;
        }
        
        h2 {
            color: #444;
            font-weight: 400;
            margin-bottom: 10px;
        }
        
        /* Form Styles */
        form {
            margin-top: 20px;
        }
        
        .input-box {
            margin-bottom: 10px;
        }
        
        .input-box input[type="text"] {
            width: 50%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        
        .input-box input[type="text"]:focus {
            border-color: #aaa;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
        }
        
        /* Button Styles */
        button[type="submit"] {
            background-color: #4CAF50;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        
        button[type="submit"]:hover {
            background-color: #3e8e41;
        }
        
        /* Checkbox Styles */
        .checkbox-column {
            margin-top: 10px;
        }
        
        .checkbox-column label {
            display: block;
            margin-bottom: 5px;
        }
        
        .checkbox-column input[type="checkbox"] {
            margin-right: 5px;
        }

        li {
			display: inline-block;
			margin-right: 250px;
		}

        input[type="submit"] {
            background-color: #4CAF50; /* Green */
            color: #ffffff; /* White */
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
          
          input[type="submit"]:hover {
            background-color: #3e8e41; /* Dark Green */
        }
          
          input[type="submit"]:active {
            background-color: #3e8e41; /* Dark Green */
            box-shadow: 0 5px #666;
            transform: translateY(4px);
        }
        
        /* Responsive Design */
        @media only screen and (max-width: 768px) {
            .container {
                margin: 20px auto;
            }
        }