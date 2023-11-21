<template>
    <!-- Root div element for the application -->
    <div id="app">
        <!-- Main section -->
        <main>
            <!-- The QueryBuilder component is used to build the query. 
                 When the data is obtained, the "updateData" method is called with the new data. -->
            <QueryBuilder class="querybuilder" @data-obtained="updateData" @query-made="querycreated" />

            <!-- The VisualQuery component is used to visualize the data.
                 The "responseData" prop is passed to it. -->
            <VisualQuery class="visualquery" :data="responseData" />

            <!-- The SaveQuery component is used to save the query.
                 The "query" prop is passed to it. When the query is saved, the "Updatequery" method is called. -->
            <SaveQuery class="savequery" :query="query" @query-saved="Updatequery" />

            <!-- The ShowQueries component is used to display the queries. -->
            <ShowQueries class="showqueries" ref="showQueries" />
        </main>
        <!-- Footer section -->
    </div>
</template>

<script>
import QueryBuilder from './components/QueryBuilder.vue'; // Importing the QueryBuilder component
import VisualQuery from './components/VisualQuery.vue'; // Importing the VisualQuery component
import SaveQuery from './components/SaveQuery.vue'; // Importing the SaveQuery component
import ShowQueries from './components/ShowQueries.vue'; // Importing the ShowQueries component

export default {
    name: "App", // Name of the Vue component
    components: {
        // Imported components
        QueryBuilder,
        VisualQuery,
        SaveQuery,
        ShowQueries,
    },
    data() {
        return {
            // The responseData data property is used to store the data obtained from the query
            responseData: null,
            // The query data property is used to store the created query
            query: null
        }
    },
    methods: {
        // The updateData method is used to update the responseData property with the new data
        updateData(newData) {
            this.responseData = newData;
        },
        // The querycreated method is used to update the query property with the created query
        querycreated(query) {
            this.query = query;
        },
        // The Updatequery method is used to reload the queries in the ShowQueries component
        Updatequery() {
            this.$refs.showQueries.loadQueries();
        }
    }
}
</script>
<style>
/*
Reset CSS: Used to remove the default styles that browsers apply to HTML elements.
*/
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/*Root for variables*/
:root {
    --with-size-page: 100%;
    --font-family: 'Good Times', sans-serif;
}

/*Sets the font size and height for the html and body elements*/
html, body {
    font-size: 62.5%;
    height: 100%;
    margin: 0;
    padding: 0;
}

/*Sets the display property of the body element to flex and its direction to column*/
body {
    display: flex;
    flex-direction: column;
}


/*Styles for the main element*/
main {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    background-color: rgba(255, 238, 238, 0.479);
    width: var(--with-size-page);
    flex-grow: 1; /* Added so that main grows to fill the space */
}

/*Styles for the savequery class*/
.savequery {
    position: relative;
    top: 40rem;
}

/*Styles for the showqueries class*/
.showqueries {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
}

/*Styles for the footer element*/

</style>