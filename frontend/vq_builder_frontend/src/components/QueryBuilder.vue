<template>
    <!-- Main container for the component -->
    <div id="query-builder">
        <!-- Main content of the component -->
        <main>
            <!-- Form for user input -->
            <div class="form-group">
                <!-- Input for entering value -->
                <label for = "term">Term: </label><br>
                <input type="text" id="term" name="term" v-model="term"><br>
                <div class = "errors" v-if = "termError" style = "color: red;"> This field is required. </div>

                <label for = "score"> Score: </label><br>
                <input type = "number" id = "score" name = "score" min = "0" step = "any" v-model = "score"><br>
                <p class = "errors">{{ errorScore }}</p>

                <label for = "rank"> Rank: </label><br>
                <input type = "number" id = "rank" name = "rank" min = "0" step = "any" v-model = "rank"><br>
                <p class = "errors">{{ errorRank }}</p>

                <label for = "week">Week (YYYY-MM-DD): </label><br>
                <input type="text" id="week" name = "week" v-model="week"><br>

                <label for = "refresh_date">Refresh Date (YYYY-MM-DD): </label><br>
                <input type="text" id="refresh_date" name = "refresh_date" v-model="refresh_date"><br>
                <!-- Button for running query -->
                <button class="runquery" v-on:click="runquery">Build</button>
            </div>
        </main>
    </div>
</template>

<script>
// Importing the axios library for making HTTP requests
import axios from 'axios';

export default {
    name: "App",
    // Defining the data properties for the component
    data: function () {
        return {
            term: null,
            score: 0,
            rank: 0,
            week: null,
            refresh_date: null,

            errorTerm: null,
            errorScore: null,
            errorRank: null,
            responseData: null,
        };
    },
    methods: {
        // Method for running the query when the form is submitted
        runquery() {
            // Check if the country and series fields are filled out
            this.termError = !this.term;

            // If either field is not filled out, stop the function
            if (this.termError) {
                return;
            }

            if (this.score < 0) {
                this.errorScore = 'Please, enter a valid score(not below 0)';
                return;
            } else {
                this.errorScore = null;
            }

            if (this.rank < 0) {
                this.errorRank = 'Please, enter a valid rank (not below 0)';
                return;
            } else {
                this.errorRank = null;
            }


            // Make a POST request to the API with the form inputs
            axios.post('http://127.0.0.1:8000', {
                term: this.term,
                score: this.score,
                rank: this.rank,
                week: this.week,
                refresh_date: this.refresh_date
            })
                .then(response => {
                    this.responseData = response.data;
                    this.$emit('data-obtained', this.responseData);
                    this.$emit('query-made', {
                        term: this.term,
                        score: this.score,
                        rank: this.rank,
                        week: this.week,
                        refresh_date: this.refresh_date
                    });

                })
                .catch(error => {
                    console.error(error);
                })
        }
    }
}
</script>

<style>
:root {
    --font-family: var(--font-family);
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    font-size: 62.5%;
}

.form-group {
    display: flex;
    flex-direction: column;
    margin: 5rem 5rem;
    border: 0.001rem solid rgb(189, 30, 6);
    border-radius: 0.5rem;
    width: 25rem;
}

.form-group label {
    margin: 0.5rem 2rem;
    font-size: 1.5rem;
    font-family: var(--font-family);
    color: black;
}

.errors {
    margin: 0rem 0rem 1.5rem 1rem;
    padding: 1em;
    height: 5%;
    color: red;
    width: 20.5rem;
    font-family: var(--font-family);
    font-size: 15px;
}

.form-group select,
.form-group input {
    width: 80%;
    padding: 0.5rem;
    font-size: 1rem;
    margin-left: 1.5rem;
    border: 0.01rem solid gray;
    border-radius: 1rem;
}

.runquery {
    margin: 2rem;
    width: 60%;
    background-color: rgb(189, 30, 6);
    /* Background color of the button */
    color: #FFFFFF;
    /* Text color */
    padding: 0.5rem;
    /* Internal spacing */
    text-decoration: none;
    /* Remove text decoration */
    font-size: 1.4rem;
    /* Font size */
    transition-duration: 0.5s;
    /* Transition duration */
    cursor: pointer;
    /* Change the cursor to a pointer */
    border: 0.1rem solid #FFC300;
    /* Neon purple border */
    border-radius: 0.5rem;
}

.runquery:hover {
    background-color: #FFC300;
}

.responseData {
    display: inline-block;
    justify-content: right;
    align-items: right;
}
</style>