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
};

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
