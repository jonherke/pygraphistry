import React, { PropTypes } from 'react';
import {
    Subject, Observable,
    Subscription, ReplaySubject
} from 'rxjs';

import {
    compose,
    getContext,
    shallowEqual
} from 'recompose';

import _ from 'underscore';

import styles from './style.less';



const propTypes = {
    opacity: React.PropTypes.number,
    background: React.PropTypes.any,
    foreground: React.PropTypes.any,

    poiEnabled: React.PropTypes.bool,
    enabled: React.PropTypes.bool,

    onClick: React.PropTypes.func,
    onFilter: React.PropTypes.func,
    onExclude: React.PropTypes.func,
    onPinChange: React.PropTypes.func,

    hideNull: React.PropTypes.bool,
    selectedColumns: React.PropTypes.object,
    labels: React.PropTypes.array
};

const defaultProps = {
    opacity: 1,
    poiEnabled: true,
    enabled: true,
    onClick: _.identity,
    onFilter: _.identity,
    onExclude: _.identity,
    onPinChange: _.identity,
    hideNull: true,
    labels: [
          {
            type: 'point',
            id: 'bullwinkle',
            title: "the greatest moose",

            showFull: true, // expanded when :hover or .on
            pinned: true,

            x: 100,
            y: 200,

            fields: {


            }
        }]
}

function LabelTitle (props) {
    return (
        <div className={styles['graph-label-title']}>
            <i className={`
                ${styles['pin']}
                ${styles['fa']}
                ${styles['fa-lg']}
                ${styles['fa-thumb-tack']}`} />
            <span className={styles['title']}>{ props.label.title }</span>
            <a className={styles['exclude-by-title']}>
                <i className={`${styles['fa']} ${styles['fa-ban']}`} />
            </a>
            <span className={styles['label-type']}>{ props.label.type }</span>
        </div>);
}

function LabelRow (props) {
    return (
        <tr className={styles['graph-label-pair']}>
            <td className={styles['graph-label-key']}>{props.key}</td>
            <td className={styles['graph-label-value']}>
                <div className={styles['graph-label-value-wrapper']}>
                    {props.value}
                    <div className={styles['graph-label-icons']}>
                        <a className={`${styles['tag-by-key-value']} ${styles['beta']}`}>
                            <i className={`${styles['fa']} ${styles['fa-tag']}`} />
                        </a>
                        <a className={styles['exclude-by-key-value']}>
                            <i className={`${styles['fa']} ${styles['fa-ban']}`} />
                        </a>
                        <a className={styles['filter-by-key-value']}>
                            <i className={`${styles['fa']} ${styles['fa-filter']}`} />
                        </a>
                    </div>
                </div>
            </td>
        </tr>);
}

function LabelContents (props) {
    return (
        <div className={styles['graph-label-contents']}>
            <table>
                <tbody>{
                    _.pairs(props.label.fields)
                        .sort(([kA], [kB]) =>
                            kA.toLowerCase() < kB.toLowerCase() ? -1
                            kA.toLowerCase() > kB.toLowerCase() ? 1
                            : 0)
                        .map( ([key, value]) => {
                            return <LabelRow {...props} key={key} value={value}/>
                        })
                }</tbody>
            </table>
        </div>);
}



class DataLabel extends React.Component {

    constructor(props) {
        super(props);
        console.log('label props', props);
    }

    render () {
        return (<div className={`
            ${styles['graph-label']}
            ${this.props.label.showFull ? styles['on'] : ''}
            ${this.props.label.pinned ? styles['clicked'] : ''}`}>
            <div className={`
                ${styles['graph-label-container']}
                ${styles['graph-label-' + this.props.label.type]}`}>

                <LabelTitle { ...this.props } />

                <LabelContents { ...this.props } />

            </div>
        </div>)
    }

}

class Labels extends React.Component {

    constructor(props) {
        super(props);
        console.log('labels props', props);
    }

    render() {

        if (!this.props.enabled) return <div className={styles['labels-container']} />;

        return (
            <div className={styles['labels-container']}>
                {
                    this.props.labels.map( (label) => (
                        <DataLabel {...this.props} label={label} /> ))
                }
            </div>
        );
    }
}



Labels.propTypes = propTypes;
Labels.defaultProps = defaultProps;

Labels = getContext({
    renderState: PropTypes.object,
    renderingScheduler: PropTypes.object,
})(Labels);


export { Labels };
