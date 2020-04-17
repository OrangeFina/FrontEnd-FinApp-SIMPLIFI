import React, {Component} from 'react';

class News extends Component {
    render() {
        return (
            <div>
                <p>{this.props.News.Title}</p>
                <p>{this.props.News.color}</p>
                <p>${this.props.News.price}</p>
            </div>
        );
    }
}

export default News;