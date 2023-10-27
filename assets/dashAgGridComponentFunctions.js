var dagcomponentfuncs = (window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {});


dagcomponentfuncs.Button = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData();
    }
    return React.createElement(
        'button',
        {
            onClick: onClick,
            className: props.className,
        },
        props.value
    );
};

dagcomponentfuncs.StockLink = function (props) {
    return React.createElement(
        'a',
        {href: props.value},
        props.value
    );
};

dagcomponentfuncs.CustomTooltip = function (props) {
    /*info = [
        React.createElement('h4', {}, props.data.ticker),
        React.createElement('div', {}, props.data.company),
        React.createElement('div', {}, props.data.price),
    ];*/
    info = "Click the link to open the tool's web page"
    return React.createElement(
        'div',
        {
            style: {
                //border: '2pt solid white',
                backgroundColor: props.color || '#D3D3D3',
                padding: 10,
                //color: 'white'
            },
        },
        info
    );
};

dagfuncs.journalColSpan = function(params) {
    return 2;
    /*if (isHeaderRow(params)) {
      return 6;
    } else if (isQuarterRow(params)) {
      return 3;
    } else {
      return 1;
    }*/
};


/*
dagcomponentfuncs.DCC_GraphClickData = function (props) {
    const {setData} = props;
    function setProps() {
        const graphProps = arguments[0];
        if (graphProps['clickData']) {
            setData(graphProps);
        }
    }
    return React.createElement(window.dash_core_components.Graph, {
        figure: props.value,
        setProps,
        style: {height: '100%'},
        config: {displayModeBar: false},
    });
};

*/

dagcomponentfuncs.CustomLoadingOverlay = function (props) {
    return React.createElement(
        'div',
        {
            style: {
                border: '1pt solid grey',
                color: props.color || 'grey',
                padding: 10,
            },
        },
        props.loadingMessage
    );
};
